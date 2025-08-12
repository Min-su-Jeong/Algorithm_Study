#include <bits/stdc++.h>
using namespace std;

const int INF = 987654321;
const int MAX = 1e6+4;
int N, dp[MAX];

void trace(int here) {
    if (here == 0) return;
    printf("%d ", here);
    if ((here % 3 == 0) && (dp[here] == dp[here/3]+1)) trace(here/3);
    else if ((here % 2 == 0) && (dp[here] == dp[here/2]+1)) trace(here/2);
    else if ((here - 1 >= 0) && (dp[here] == dp[here-1]+1)) trace(here-1);
    return;
}

int main() {
    scanf("%d", &N);
    fill(dp, dp + MAX, INF);

    dp[1] = 0;
    for (int i=1; i<=N; i++) {
        if (i % 3 == 0) dp[i] = min(dp[i], dp[i/3]+1);
        if (i % 2 == 0) dp[i] = min(dp[i], dp[i/2]+1);
        dp[i] = min(dp[i], dp[i-1]+1);
    }
    printf("%d\n", dp[N]);
    trace(N);
    return 0;
}