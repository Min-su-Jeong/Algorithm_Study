#include <bits/stdc++.h>
using namespace std;

#define MAX_N 60000000004
#define MAX_M 10004

typedef long long ll;
ll N, M, a[MAX_M], ret;

bool check(ll mid) {
    ll tmp = M;
    for (ll i=0; i<M; i++) tmp += mid / a[i];
    return tmp >= N;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M;
    for (ll i=0; i<M; i++) cin >> a[i];
    if (N <= M) {
        cout << N << '\n';
        return 0;
    }
    
    ll lo = 0, hi = MAX_N;
    while(lo <= hi) {
        ll mid = (lo + hi) / (1LL * 2);
        if (check(mid)) {
            ret = mid;
            hi = mid - 1;
        } else lo = mid + 1;
    }
    
    ll tmp = M;
    for (ll i=0; i<M; i++) tmp += ((ret - 1) / a[i]); 
    for (ll i=0; i<M; i++) {
        if(ret % a[i] == 0) tmp++; 
        if(tmp == N){
            cout << i + 1 << '\n';
            return 0; 
        }
    }
    return 0;
}