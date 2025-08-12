#include <bits/stdc++.h>
using namespace std;

const int MAX = 2001;
int N, M, from, to, a[MAX], dp[MAX][MAX];

int main() {
    scanf("%d", &N);
    for (int i=1; i<=N; i++) scanf("%d", &a[i]);

    for (int i=1; i<=N; i++) {
        dp[i][i] = 1;
        if (a[i] == a[i+1]) dp[i][i+1] = 1;
    }
    for (int _size=2; _size<=N; _size++) {
        for (int i=1; i<=N-_size; i++) {
            if (a[i] == a[i+_size] && dp[i+1][i+_size-1]) {
                dp[i][i+_size] = 1;
            }
        }
    }

    scanf("%d", &M);
    while (M--) {
        scanf("%d %d", &from, &to);
        printf("%d\n", dp[from][to]);
    }
    return 0;
}