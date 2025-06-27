#include <bits/stdc++.h>
using namespace std;

const int MAX = 254;
const int dx[8] = {0, -1, 0, 1, -1, -1, 1, 1};
const int dy[8] = {1, 0, -1, 0, -1, 1, -1, 1};
int M, N, y, x, ret, graph[MAX][MAX];
bool visited[MAX][MAX];

void bfs(int y, int x) {
    visited[y][x] = 1;
    queue<pair<int, int>> q;
    q.push({y, x});

    while (q.size()) {
        tie(y, x) = q.front();
        q.pop();
        for (int i=0; i<8; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (ny < 0 || nx < 0 || ny >= M || nx >= N) continue;
            if (graph[ny][nx] == 0 || visited[ny][nx]) continue;
            visited[ny][nx] = 1;
            q.push({ny, nx});
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> M >> N;
    for (int i=0; i<M; i++) {
        for (int j=0; j<N; j++) {
            cin >> graph[i][j];
        }
    }

    for (int i=0; i<M; i++) {
        for (int j=0; j<N; j++) {
            if (graph[i][j] == 0 || visited[i][j]) continue;
            bfs(i, j);
            ret++;
        }
    }
    cout << ret << '\n';
    return 0;
}