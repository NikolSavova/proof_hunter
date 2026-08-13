#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <random>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using std::array; using std::string; using std::vector;

struct State {
    int target, bound;
    array<vector<int>,5> x;
    array<vector<uint8_t>,5> occupied;
    array<array<vector<int16_t>,5>,5> ps;
    int covered_count=0; int64_t weighted=0;

    State(int m,int b):target(m),bound(b){
        for(auto &v:occupied)v.assign(bound+1,0);
        for(int a=0;a<5;++a)for(int b2=0;b2<5;++b2)ps[a][b2].assign(target,0);
    }
    bool has(int a,int b,int q)const{return q>=0&&q<target&&ps[std::min(a,b)][std::max(a,b)][q];}
    bool con(int a,int b,int q)const{return has(a,b,q-1)&&has(a,b,q);}
    bool covered(int q)const{
        return has(0,1,q)||has(0,2,q)||has(0,3,q)
          ||con(1,2,q)||con(1,3,q)||con(0,4,q)||con(1,4,q)
          ||(has(0,3,q-1)&&has(0,4,q))
          ||(has(1,4,q-1)&&has(1,3,q))
          ||(has(2,3,q-1)&&has(2,4,q))
          ||(has(2,4,q-1)&&has(2,3,q));
    }
    int prefix()const{int q=0;while(q<target&&covered(q))++q;return q;}
    int64_t score()const{return 1000000LL*prefix()+1000LL*covered_count+weighted;}
    void initialize(const array<vector<int>,5>& sets){
        x=sets;
        for(int c=0;c<5;++c){
            std::fill(occupied[c].begin(),occupied[c].end(),0);
            for(int p:x[c]){if(p<0||p>bound||occupied[c][p])std::exit(2);occupied[c][p]=1;}
        }
        for(int a=0;a<5;++a)for(int b=a+1;b<5;++b){
            std::fill(ps[a][b].begin(),ps[a][b].end(),0);
            if(a==3&&b==4)continue;
            for(int u:x[a])for(int v:x[b])if(u+v<target)++ps[a][b][u+v];
        }
        covered_count=0;weighted=0;
        for(int q=0;q<target;++q)if(covered(q)){++covered_count;weighted+=target-q;}
    }
    bool move(int c,int idx,int replacement){
        if(replacement<0||replacement>bound||occupied[c][replacement])return false;
        int old=x[c][idx]; vector<int> affected; vector<uint8_t> seen(target,0);
        if((c==0||c==1)&&old==0)return false; // retain a direct witness for square zero
        auto mark=[&](int q){if(q>=0&&q<target&&!seen[q]){seen[q]=1;affected.push_back(q);}};
        for(int d=0;d<5;++d)if(d!=c&&!(std::min(c,d)==3&&std::max(c,d)==4))
            for(int v:x[d]){mark(old+v);mark(old+v+1);mark(replacement+v);mark(replacement+v+1);}
        for(int q:affected)if(covered(q)){--covered_count;weighted-=target-q;}
        for(int d=0;d<5;++d)if(d!=c&&!(std::min(c,d)==3&&std::max(c,d)==4)){
            int a=std::min(c,d),b=std::max(c,d);
            for(int v:x[d]){if(old+v<target)--ps[a][b][old+v];if(replacement+v<target)++ps[a][b][replacement+v];}
        }
        occupied[c][old]=0;occupied[c][replacement]=1;x[c][idx]=replacement;
        for(int q:affected)if(covered(q)){++covered_count;weighted+=target-q;}
        return true;
    }
};

struct Opt{int target=94,bound=93;array<int,5> counts{5,5,4,2,2};int64_t steps=100000000;int restarts=50;uint64_t seed=791;string output;};
Opt parse(int n,char**v){Opt o;for(int i=1;i<n;++i){string a=v[i];auto nx=[&](){return string(v[++i]);};
 if(a=="--target")o.target=std::stoi(nx());else if(a=="--bound")o.bound=std::stoi(nx());
 else if(a=="--counts"){string s=nx();std::replace(s.begin(),s.end(),',',' ');std::istringstream in(s);for(int&z:o.counts)in>>z;}
 else if(a=="--steps")o.steps=std::stoll(nx());else if(a=="--restarts")o.restarts=std::stoi(nx());
 else if(a=="--seed")o.seed=std::stoull(nx());else if(a=="--output")o.output=nx();else std::exit(2);}return o;}

array<vector<int>,5> initial(const Opt&o,std::mt19937_64&r){
 array<vector<int>,5>s; std::uniform_int_distribution<int>pos(0,o.bound);
 if(o.target>500&&o.counts[0]>=8&&o.counts[1]>=17&&o.counts[2]>=17){
  s[0]={0,5,112,117,122,127,132,137};s[1]={10,16,22,28,34,40,46,52,58,64,70,76,82,88,94,100,106};
  s[2]={0,1,2,3,4,224,225,226,227,228,229,367,368,369,370,371,372};
  if(o.counts[3])s[3]={510};if(o.counts[4])s[4]={511};
 }
 for(int c=0;c<5;++c){std::set<int>u(s[c].begin(),s[c].end());while((int)u.size()>o.counts[c])u.erase(std::prev(u.end()));
  if(u.empty()&&(c==0||c==1))u.insert(0);while((int)u.size()<o.counts[c])u.insert(pos(r));s[c]=vector<int>(u.begin(),u.end());}return s;
}

string placement(const array<vector<int>,5>&x){const char*n[5]={"I","J","K","L0","L1"};std::ostringstream o;o<<"{\n";
 for(int c=0;c<5;++c){auto v=x[c];std::sort(v.begin(),v.end());o<<"    \""<<n[c]<<"\": [";for(size_t i=0;i<v.size();++i){if(i)o<<", ";o<<v[i];}o<<"]"<<(c==4?'\n':',') ;}o<<"  }";return o.str();}

int main(int argc,char**argv){Opt o=parse(argc,argv);std::mt19937_64 rng(o.seed);std::uniform_real_distribution<double>unit(0,1);
 auto start=std::chrono::steady_clock::now();int bestc=-1,bestp=-1;int64_t bestscore=-1,eval=0,accepted=0;array<vector<int>,5>best;
 // Each entry is a pair type and whether the desired sum is q-1 rather than q.
 const vector<std::array<int,3>> routes={{0,1,0},{0,2,0},{0,3,0},{1,2,0},{1,2,1},{1,3,0},{1,3,1},
  {0,4,0},{0,4,1},{1,4,0},{1,4,1},{0,3,1},{0,4,0},{1,4,1},{1,3,0},
  {2,3,1},{2,4,0},{2,4,1},{2,3,0}};
 for(int rr=0;rr<o.restarts&&eval<o.steps;++rr){State st(o.target,o.bound);st.initialize(initial(o,rng));int64_t quota=(o.steps+o.restarts-1)/o.restarts;
  for(int64_t z=0;z<quota&&eval<o.steps;++z,++eval){int64_t before=st.score();struct Ch{int c,i,old;};vector<Ch>ch;
   int moves=unit(rng)<.18?2:1;
   for(int mv=0;mv<moves;++mv){int c,idx,p;
    if(unit(rng)<.55&&st.covered_count<o.target){vector<int>holes;for(int q=0;q<o.target;++q)if(!st.covered(q))holes.push_back(q);int q=holes[rng()%holes.size()];auto rt=routes[rng()%routes.size()];int a=rt[0],b=rt[1],req=q-rt[2];c=(rng()&1)?a:b;int d=c==a?b:a;idx=rng()%st.x[c].size();p=req-st.x[d][rng()%st.x[d].size()];}
    else{c=rng()%5;idx=rng()%st.x[c].size();int old=st.x[c][idx];if(unit(rng)<.72){int d=1+(int)(-std::log(std::max(1e-12,unit(rng)))*6);p=old+((rng()&1)?d:-d);}else p=rng()%(o.bound+1);}
    int old=st.x[c][idx];if(st.move(c,idx,p))ch.push_back({c,idx,old});}
   if(ch.empty())continue;int64_t after=st.score();double f=(double)z/std::max<int64_t>(1,quota-1);double temp=2500000*std::pow(300.0/2500000,f);
   if(after<before&&unit(rng)>=std::exp((double)(after-before)/temp)){for(auto it=ch.rbegin();it!=ch.rend();++it)if(!st.move(it->c,it->i,it->old))return 3;}else ++accepted;
   int p=st.prefix();if(p>bestp||(p==bestp&&st.covered_count>bestc)||(p==bestp&&st.covered_count==bestc&&st.score()>bestscore)){bestc=st.covered_count;bestp=p;bestscore=st.score();best=st.x;}
   if(bestp==o.target)goto done;
  }
  std::cerr<<"restart "<<rr+1<<" best="<<bestc<<"/"<<o.target<<" prefix="<<bestp<<"\n";
 }
done: double sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();std::ostringstream out;out<<"{\n  \"status\": \""<<(bestp==o.target?"FOUND":"NO_SOLUTION_FOUND")<<"\",\n  \"target\": "<<o.target<<",\n  \"counts\": [";for(int i=0;i<5;++i){if(i)out<<", ";out<<o.counts[i];}out<<"],\n  \"proposals\": "<<eval<<",\n  \"accepted\": "<<accepted<<",\n  \"seconds\": "<<sec<<",\n  \"best_coverage\": "<<bestc<<",\n  \"best_prefix\": "<<bestp<<",\n  \"placement\": "<<placement(best)<<"\n}\n";std::cout<<out.str();if(!o.output.empty()){std::ofstream f(o.output);f<<out.str();}return bestp==o.target?0:1;}
