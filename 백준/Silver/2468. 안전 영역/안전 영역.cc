#include <bits/stdc++.h>
using namespace std;

const int MAX = 101;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int N, ret=1; // 반례 방지
int graph[MAX][MAX];
bool visited[MAX][MAX];

void dfs(int y, int x, int d) {
    visited[y][x] = true;

    for (int i=0; i<4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];

        if (ny < 0 || nx < 0 || nx >= N || ny >= N) continue;
        if (graph[ny][nx] > d && !visited[ny][nx]) {
            dfs(ny, nx, d);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> graph[i][j];
        }
    }

    for (int d=1; d<101; d++) {
        fill(&visited[0][0], &visited[0][0] + MAX * MAX, 0);
        int cnt = 0;

        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                if (graph[i][j] > d && !visited[i][j]) {
                    dfs(i, j, d);
                    cnt++;
                }
            }
        }
        ret = max(ret, cnt);
    }
    cout << ret << '\n';
    return 0;
}