#include <bits/stdc++.h>
using namespace std;

const int MAX = 54;
const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {1, 0, -1, 0};
string s;
char a[MAX][MAX];
int N, M, dp[MAX][MAX];
bool visited[MAX][MAX];

bool inRange(int y, int x) {
    return (1 <= y && y <= N && 1 <= x && x <= M);
}

int move(int y, int x) {
    if (!inRange(y, x) || a[y][x] == 'H') return 0;
    if (visited[y][x]) {
        cout << -1 << '\n';
        exit(0);
    }
    int &ret = dp[y][x];
    if (ret) return ret;

    visited[y][x] = 1;
    int val = (int)a[y][x] - '0';
    for (int i=0; i<4; i++) {
        int ny = y + dy[i] * val;
        int nx = x + dx[i] * val;
        ret = max(ret, move(ny, nx) + 1);
    }
    visited[y][x] = 0;
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M;
    for (int i=1; i<=N; i++) {
        cin >> s;
        for (int j=1; j<=M; j++) {
            a[i][j] = s[j-1];
        }
    }
    cout << move(1, 1) << '\n';
    return 0;
}