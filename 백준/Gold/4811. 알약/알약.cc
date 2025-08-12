#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll N, dp[31][31];

ll go(int full, int half) {
    if (full == 0 && half == 0) return 1;

    ll &ret = dp[full][half];
    if (ret) return dp[full][half];
    if (full > 0) ret += go(full-1, half+1);
    if (half > 0) ret += go(full, half-1);

    return ret;
}

int main() {
    while (true) {
        scanf("%d", &N); if (N == 0) break;
        printf("%lld\n", go(N, 0));
    }
    return 0;
}