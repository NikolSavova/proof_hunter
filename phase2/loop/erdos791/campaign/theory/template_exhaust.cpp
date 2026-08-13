// Exhaust a broad rectangular family of coherent AP/interval layouts around
// (but not restricted to local coordinate moves from) Kohonen's construction.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
using V=std::vector<int>;
static V ap(int s,int d,int n){V a;for(int i=0;i<n;i++)a.push_back(s+d*i);return a;}
struct E{int pref=0,cnt=0;};
static E ev(const V&I,const V&J,const V&K){
  constexpr int H=511; std::array<uint8_t,H>ij{},ik{},jk{};
  for(int x:I)for(int y:J)if(x+y<H)ij[x+y]=1;
  for(int x:I)for(int y:K)if(x+y<H)ik[x+y]=1;
  for(int x:J)for(int y:K)if(x+y<H)jk[x+y]=1;
  E e;for(int q=0;q<H;q++){bool c=ij[q]||ik[q]||(q&&jk[q-1]&&jk[q]);e.cnt+=c;if(e.pref==q&&c)e.pref++;}return e;
}
static void pv(const char*n,const V&a){std::cout<<n<<"=";for(int x:a)std::cout<<x<<",";std::cout<<"\n";}
int main(){
  long long tested=0; E best{}; V bi,bj,bk;
  // Initial interval and low I/J geometry is allowed to change.  The two high
  // K intervals keep length six, while both long AP starts and spacings vary.
  for(int x=5;x<=5;x++)for(int k0=5;k0<=5;k0++)
  for(int is=96;is<=130;is++)for(int id=4;id<=7;id++)
  for(int js=6;js<=14;js++)for(int jd=5;jd<=7;jd++){
    V I{0,x};auto ih=ap(is,id,6);I.insert(I.end(),ih.begin(),ih.end());
    V J=ap(js,jd,17),K0=ap(0,1,k0);
    // Keep total ell=42 by transferring changes in the low K interval to the
    // last interval.  Thus c2=11-k0 and all type counts remain (8,17,17).
    int c2=11-k0;if(c2<1)continue;
    for(int k1=205;k1<=245;k1++)for(int k2=340;k2<=400;k2++){
      V K=K0,a=ap(k1,1,6),b=ap(k2,1,c2);K.insert(K.end(),a.begin(),a.end());K.insert(K.end(),b.begin(),b.end());
      E e=ev(I,J,K);tested++;
      if(e.cnt>best.cnt||(e.cnt==best.cnt&&e.pref>best.pref)){best=e;bi=I;bj=J;bk=K;std::cout<<"best tested="<<tested<<" count="<<e.cnt<<" prefix="<<e.pref<<"\n";pv("I",I);pv("J",J);pv("K",K);}
      if(e.pref>=511){std::cout<<"FOUND tested="<<tested<<"\n";return 0;}
    }
  }
  std::cout<<"NO_TARGET tested="<<tested<<" best_count="<<best.cnt<<" best_prefix="<<best.pref<<"\n";pv("I",bi);pv("J",bj);pv("K",bk);return 1;
}
