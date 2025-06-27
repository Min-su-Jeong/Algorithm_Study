#include <bits/stdc++.h>
using namespace std;

const int MAX = 1004;
const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {1, 0, -1, 0};
int M, N, y, x, graph[MAX][MAX];
bool visited[MAX][MAX];
queue<pair<int, int>> q;

bool bfs() {
    while (q.size()) {
        tie(y, x) = q.front();
        q.pop();
        if (y == M-1) return true;
        for (int i=0; i<4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (ny < 0 || nx < 0 || ny >= M || nx >= N) continue;
            if (graph[ny][nx] == 1 || visited[ny][nx]) continue;
            visited[ny][nx] = 1;
            q.push({ny, nx});
        }
    }
    return false;
}

int main() {
    scanf("%d %d", &M, &N);

    for (int i=0; i<M; i++) {
        for (int j=0; j<N; j++) {
            scanf("%1d", &graph[i][j]);
            if (i==0 && graph[i][j] == 0) {
                visited[i][j] = 1;
                q.push({i, j});
            }
        }
    }

    if (bfs()) printf("YES\n");
    else printf("NO\n");
    return 0;
}