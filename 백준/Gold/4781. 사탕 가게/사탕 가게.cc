#include <bits/stdc++.h>
using namespace std;

const int MAX = 10004;
int n, m1, m2, c, p1, p2, dp[MAX];

int main() {
    while (true) {
        scanf("%d %d.%d", &n, &m1, &m2);
        if (n == 0) break;

        int cost = m1 * 100 + m2;
        fill(dp, dp+MAX, 0);
        for (int i = 0; i<n; i++) {
            scanf("%d %d.%d", &c, &p1, &p2);
            int p = p1 * 100 + p2;
            for (int j=p; j<=cost; j++) {
                dp[j] = max(dp[j], dp[j-p]+c);
            }
        }
        printf("%d\n", dp[cost]);
    }
    return 0;
}