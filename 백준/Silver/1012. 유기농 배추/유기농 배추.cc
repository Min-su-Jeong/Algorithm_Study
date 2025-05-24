#include <bits/stdc++.h>
using namespace std;

const int MAX = 54;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int M, N, K, X, Y, T, nx, ny, ret;
int graph[MAX][MAX];
bool visited[MAX][MAX];

void dfs(int y, int x) {
    visited[y][x] = true;
    for (int i=0; i<4; i++) {
        nx = x + dx[i];
        ny = y + dy[i];
        if (ny < 0 || ny >= N || nx < 0 || nx >= M) continue;
        if (graph[ny][nx] == 1 && !visited[ny][nx]) {
            dfs(ny, nx);
        }
    }
    return;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> T;

    while(T--) {
        ret = 0;
        fill(&graph[0][0], &graph[0][0] + MAX * MAX, 0);
        fill(&visited[0][0], &visited[0][0] + MAX * MAX, 0);
        
        cin >> M >> N >> K;
        for (int i=0; i<K; i++) {
            cin >> X >> Y;
            graph[Y][X] = 1;
        }

        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (graph[i][j] == 1 && !visited[i][j]) {
                    dfs(i, j);
                    ret++;
                }
            }
        }
        cout << ret << '\n';
    }
    return 0;
}