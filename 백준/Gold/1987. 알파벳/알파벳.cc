#include <bits/stdc++.h>
using namespace std;

const int MAX = 27;
const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {1, 0, -1, 0};
int R, C, y, x, ret, graph[MAX][MAX];
bool visited[MAX];
string s;

void go(int y, int x, int cnt) {
    ret = max(ret, cnt);
    for (int i=0; i<4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];
        if (ny < 0 || nx < 0 || ny >= R || nx >= C) continue;
        int next = graph[ny][nx];
        if (!visited[next]) {
            visited[next] = 1;
            go(ny, nx, cnt+1);
            visited[next] = 0;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> R >> C;
    for (int i=0; i<R; i++) {
        cin >> s;
        for (int j=0; j<C; j++) {
            graph[i][j] = s[j] - 'A';
        }
    }

    visited[graph[0][0]] = 1;
    go(0, 0, 1);

    cout << ret << '\n';
}