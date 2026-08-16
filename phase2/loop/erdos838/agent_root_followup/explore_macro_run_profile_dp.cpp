#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <limits>
#include <numeric>
#include <string>
#include <utility>
#include <vector>

using u64 = std::uint64_t;
using u128 = unsigned __int128;

static std::string show(u128 x) {
    if (!x) return "0";
    std::string s;
    while (x) {
        s.push_back(char('0'+x%10));
        x/=10;
    }
    std::reverse(s.begin(),s.end());
    return s;
}

static long double logarithm2(u128 x) {
    return std::log2(std::stold(show(x)));
}

static std::pair<u64,u64> chain_counts(
    const std::vector<std::int8_t>& signs, const std::vector<int>& order) {
    int n=int(order.size());
    std::vector<u64> cap(n*n),cup(n*n);
    u64 C=n,U=n;
    for (int i=0;i<n;i++) for (int j=i+1;j<n;j++) {
        u64 a=1,b=1;
        for (int h=0;h<i;h++) {
            int s=signs[(order[h]*n+order[i])*n+order[j]];
            if (s<0) a+=cap[h*n+i]; else b+=cup[h*n+i];
        }
        cap[i*n+j]=a;cup[i*n+j]=b;C+=a;U+=b;
    }
    return {C,U};
}

struct State {
    u128 C=0,U=0,W=0;
    std::array<std::uint16_t,16> path{};
    int depth=0;
};

static std::vector<State> pareto(std::vector<State> states) {
    std::sort(states.begin(),states.end(),[](const State& a,const State& b){
        if (a.C!=b.C) return a.C<b.C;
        if (a.U!=b.U) return a.U<b.U;
        return a.W<b.W;
    });
    std::vector<u128> us;
    us.reserve(states.size());
    for (const auto& z:states) us.push_back(z.U);
    std::sort(us.begin(),us.end());
    us.erase(std::unique(us.begin(),us.end()),us.end());
    const u128 INF=~u128(0);
    std::vector<u128> tree(us.size()+1,INF);
    auto query=[&](std::size_t i) {
        u128 answer=INF;
        while (i) {answer=std::min(answer,tree[i]);i-=i&-i;}
        return answer;
    };
    auto update=[&](std::size_t i,u128 value) {
        while (i<tree.size()) {tree[i]=std::min(tree[i],value);i+=i&-i;}
    };
    std::vector<State> out;
    for (auto& z:states) {
        std::size_t ui=std::lower_bound(us.begin(),us.end(),z.U)-us.begin()+1;
        if (query(ui)<=z.W) continue;
        out.push_back(z);
        update(ui,z.W);
    }
    return out;
}

int main(int argc,char** argv) {
    int maxq=argc>1?std::stoi(argv[1]):6;
    if (maxq>16) return 3;
    int n;if (!(std::cin>>n)) return 2;
    std::vector<std::int8_t> signs(n*n*n);
    for (int i=0;i<n;i++) for (int j=i+1;j<n;j++) for (int k=j+1;k<n;k++) {
        int s;std::cin>>s;
        signs[(i*n+j)*n+k]=s;signs[(j*n+k)*n+i]=s;signs[(k*n+i)*n+j]=s;
        signs[(i*n+k)*n+j]=-s;signs[(k*n+j)*n+i]=-s;signs[(j*n+i)*n+k]=-s;
    }
    int order_count;std::cin>>order_count;
    std::vector<std::pair<u64,u64>> profiles;
    for (int q=0;q<order_count;q++) {
        std::vector<int> order(n);
        for (int& x:order) std::cin>>x;
        profiles.push_back(chain_counts(signs,order));
        std::reverse(order.begin(),order.end());
        profiles.push_back(chain_counts(signs,order));
    }
    std::sort(profiles.begin(),profiles.end());
    profiles.erase(std::unique(profiles.begin(),profiles.end()),profiles.end());
    std::vector<std::pair<u64,u64>> pfront;
    u64 bestU=std::numeric_limits<u64>::max();
    for (auto p:profiles) if (p.second<bestU) {
        pfront.push_back(p);bestU=p.second;
    }
    profiles=pfront;

    const u128 childW=11358202734ULL;
    std::vector<State> frontier(1);
    frontier[0].C=frontier[0].U=frontier[0].W=1; // first singleton
    u128 prefix_size=1;
    std::cout<<"profile_frontier="<<profiles.size()
             <<" C_range=("<<profiles.front().first<<","
             <<profiles.back().first<<")\n";
    for (int q=1;q<=maxq;q++) {
        std::vector<State> candidates;
        candidates.reserve(frontier.size()*profiles.size());
        for (const auto& old:frontier) for (int pi=0;pi<int(profiles.size());pi++) {
            auto [c,u]=profiles[pi];
            State z;
            z.C=c+u128(n+1)*old.C;
            z.U=old.U+(prefix_size+1)*u;
            z.W=old.W+childW+old.C*u;
            z.path=old.path;z.path[q-1]=pi;z.depth=q;
            candidates.push_back(z);
        }
        frontier=pareto(std::move(candidates));
        prefix_size+=n;
        u128 best=~u128(0);const State* witness=nullptr;
        for (const auto& z:frontier) {
            u128 finalW=z.W+1+z.C; // append final singleton
            if (finalW<best) {best=finalW;witness=&z;}
        }
        int total_n=q*n+2;
        long double coefficient=logarithm2(best)
            /(std::log2((long double)total_n)*std::log2((long double)total_n));
        std::cout<<"q="<<q<<" n="<<total_n<<" frontier="<<frontier.size()
                 <<" W="<<show(best)<<" coeff="<<(double)coefficient
                 <<" profiles=";
        for (int i=0;i<q;i++) {
            auto p=profiles[witness->path[i]];
            std::cout<<"("<<p.first<<","<<p.second<<")";
            if (i+1<q) std::cout<<",";
        }
        std::cout<<"\n";
    }
}
