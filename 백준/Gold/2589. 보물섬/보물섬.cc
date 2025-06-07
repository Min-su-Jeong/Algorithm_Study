#include <bits/stdc++.h>
using namespace std;

const int MAX = 51;
const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, 1, 0, -1};
int r, c, ret, visited[MAX][MAX];
char graph[MAX][MAX];

void bfs(int y, int x) {
    memset(visited, 0, sizeof(visited));
    visited[y][x] = 1;

    queue<pair<int, int>> q;
    q.push({y, x});
    
    while (q.size()) {
        tie(y, x) = q.front(); q.pop();
        for (int i=0; i<4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];

            if (ny < 0 || nx < 0 || ny >= r || nx >= c) continue;
            if (visited[ny][nx] || graph[ny][nx] == 'W') continue;
            visited[ny][nx] = visited[y][x] + 1;
            ret = max(ret, visited[ny][nx]);
            q.push({ny, nx});
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> r >> c;
    for (int i=0; i<r; i++) {
        for (int j=0; j<c; j++) {
            cin >> graph[i][j];
        }
    }

    for (int i=0; i<r; i++) {
        for (int j=0; j<c; j++) {
            if (graph[i][j] == 'L') bfs(i, j);
        }
    }
    cout << ret-1 << '\n';

    return 0;
}