#include <bits/stdc++.h>
using namespace std;

const int INF = 987654321;
const int MAX = 10004;
int n, k, v, dp[MAX];

int main() {
    fill(dp, dp+MAX, INF);
    dp[0] = 0;

    scanf("%d %d", &n, &k);
    for (int i=0; i<n; i++) {
        scanf("%d", &v);
        for (int j=v; j<=k; j++) {
            dp[j] = min(dp[j], dp[j-v]+1);
        }
    }
    if (dp[k] == INF) printf("%d", -1);
    else printf("%d", dp[k]);
    return 0;
}