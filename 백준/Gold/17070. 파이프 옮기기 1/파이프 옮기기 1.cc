#include <bits/stdc++.h>
using namespace std;

const int MAX = 20;
int N, a[MAX][MAX], dp[MAX][MAX][3];

bool check(int y, int x, int d) {
    if (d == 0 || d == 2) {
        if (!a[y][x]) return true;
    } else if (d == 1) {
        if (a[y][x] == 0 && a[y-1][x] == 0 && a[y][x-1] == 0) return true;
    }
    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    for (int i=1; i<=N; i++) {
        for (int j=1; j<=N; j++) {
            cin >> a[i][j];
        }
    }

    // 0: 가로, 1: 대각, 2: 세로
    dp[1][2][0] = 1;
    for (int i=1; i<=N; i++) {
        for (int j=1; j<=N; j++) {
            if (check(i, j+1, 0)) dp[i][j+1][0] += dp[i][j][0];
            if (check(i+1, j+1, 1)) dp[i+1][j+1][1] += dp[i][j][0];

            if (check(i, j+1, 0)) dp[i][j+1][0] += dp[i][j][1];
            if (check(i+1, j+1, 1)) dp[i+1][j+1][1] += dp[i][j][1];
            if (check(i+1, j, 2)) dp[i+1][j][2] += dp[i][j][1];

            if (check(i+1, j+1, 1)) dp[i+1][j+1][1] += dp[i][j][2];
            if (check(i+1, j, 2)) dp[i+1][j][2] += dp[i][j][2];
        }
    }
    int ret = dp[N][N][0] + dp[N][N][1] + dp[N][N][2];
    cout << ret << '\n';
    return 0;
}