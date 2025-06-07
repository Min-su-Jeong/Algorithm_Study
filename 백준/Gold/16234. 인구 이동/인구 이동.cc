#include <bits/stdc++.h>
using namespace std;

const int MAX = 51;
const int dx[] = {0, -1, 0, 1};
const int dy[] = {1, 0, -1, 0};
int N, L, R, sum, ret, graph[MAX][MAX];
bool visited[MAX][MAX];
vector<pair<int, int>> v;

void dfs(int y, int x, vector<pair<int, int>> &v) {
    for (int i=0; i<4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];
        if (ny < 0 || ny >= N || nx < 0 || nx >= N || visited[ny][nx]) continue;

        int gap = abs(graph[ny][nx] - graph[y][x]);
        if (gap >= L && gap <= R) {
            visited[ny][nx] = 1;
            v.push_back({ny, nx});
            sum += graph[ny][nx];
            dfs(ny, nx, v);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N >> L >> R;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> graph[i][j];
        }
    }

    while (true) {
        bool flag = 0;
        fill(&visited[0][0], &visited[0][0] + MAX * MAX, 0);
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                if (!visited[i][j]) {
                    v.clear();
                    v.push_back({i, j});
                    visited[i][j] = 1;
                    sum = graph[i][j];
                    
                    dfs(i, j, v);
                    if (v.size() == 1) continue;

                    int area = sum / v.size();
                    for (auto it: v) graph[it.first][it.second] = area;
                    flag = 1;
                }
            }
        }
        if (!flag) break;
        ret++;
    }
    cout << ret << '\n';

    return 0;
}