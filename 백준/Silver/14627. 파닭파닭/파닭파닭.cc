#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll S, C, a[1000001], sum, ret;

bool check(ll mid) {
    ll cnt = 0;
    for (int i=0; i<S; i++) {
        cnt += a[i] / mid;
    }
    return cnt >= C;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> S >> C;
    for (int i=0; i<S; i++) {
        cin >> a[i];
        sum += a[i];
    }

    ll lo = 1, hi = 1e9, mid;
    while (lo <= hi) {
        mid = (lo + hi) / (1LL * 2);
        if (check(mid)) {
            ret = mid;
            lo = mid + 1;
        } else hi = mid - 1;
    }
    cout << sum - ret * C << '\n';

    return 0;
}