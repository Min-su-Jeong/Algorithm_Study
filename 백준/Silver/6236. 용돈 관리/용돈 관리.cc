#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MAX = 100001;
ll N, M, mx, a[MAX], ret=INT_MAX;

bool check(int mid) {
    int cnt = 1;
    ll tmp = mid;
    for (int i=0; i<N; i++) {
        if (mid - a[i] < 0) {
            mid = tmp;
            cnt++;
        }
        mid -= a[i];
    }
    return cnt <= M;
}

int main() {
    scanf("%d %d", &N, &M);
    for (int i=0; i<N; i++) {
        scanf("%d", a+i);
        mx = max(mx, a[i]);
    }

    ll l=mx, r=1000000001;
    while (l <= r) {
        ll mid = (l+r) / 2;
        if (check(mid)) {
            ret = mid;
            r = mid - 1;
        } else l = mid + 1;
    }
    cout << ret << '\n';

    return 0;
}