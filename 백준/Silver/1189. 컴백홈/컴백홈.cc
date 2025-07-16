#include <bits/stdc++.h>
using namespace std;

const int MAX = 10;
const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {-1, 0, 1, 0};
int R, C, K, visited[MAX][MAX];
char a[MAX][MAX];

int go(int y, int x) {
    if (y == 0 && x == C-1) {
        if (visited[y][x] == K) return 1;
        else return 0;
    }
    int ret = 0;
    for (int i=0; i<4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];
        if (ny < 0 || ny >= R || nx < 0 || nx >= C) continue;
        if (visited[ny][nx] || a[ny][nx] == 'T') continue;
        visited[ny][nx] = visited[y][x] + 1;
        ret += go(ny, nx);
        visited[ny][nx] = 0;
    }
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> R >> C >> K;
    for (int i=0; i<R; i++) cin >> a[i];

    visited[R-1][0] = 1;
    cout << go(R-1, 0) << '\n';

    return 0;
}