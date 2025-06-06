#include <bits/stdc++.h>
using namespace std;

const int MAX = 101;
const int dx[4] = {-1, 1, 0, 0};
const int dy[4] = {0, 0, -1, 1};
int N, M, x, y, visited[MAX][MAX], graph[MAX][MAX];

int main() {
    cin >> N >> M;
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            scanf("%1d", &graph[i][j]);
        }
    }
    
    queue<pair<int, int>> q;
    q.push({0, 0});
    visited[0][0] = 1;

    while (q.size()) {
        tie(y, x) = q.front(); q.pop();

        for (int i=0; i<4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];

            if (ny < 0 || nx < 0 || ny >= N || nx >= M) continue;
            if (graph[ny][nx] == 0 || visited[ny][nx]) continue;
            visited[ny][nx] = visited[y][x] + 1;
            q.push({ny, nx});
        }
    }
    printf("%d", visited[N-1][M-1]);

    return 0;
}