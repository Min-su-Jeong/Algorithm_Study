#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MAX = 300001;
ll N, M, a[MAX], ret=INT_MAX;

bool check(ll mid) {
    ll num = 0;
    for (int i=0; i<M; i++) {
        num += a[i] / mid;
        if (a[i] % mid) num++;
    }
    return N >= num;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M;
    ll l=1, r=0, mid;
    for (int i=0; i<M; i++) {
        cin >> a[i];
        r = max(r, a[i]);
    }
    while(l <= r) {
        mid = (l + r) / 2;
        if (check(mid)) {
            ret = min(ret, mid);
            r = mid - 1;
        } else l = mid + 1;
    }
    cout << ret << '\n';

    return 0;
}