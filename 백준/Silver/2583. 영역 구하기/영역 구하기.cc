#include <bits/stdc++.h>
using namespace std;
#define y1 aa

const int MAX = 104;
const int dx[4] = {-1, 1, 0, 0};
const int dy[4] = {0, 0, -1, 1};
int M, N, K, x1, x2, y1, y2;
int graph[MAX][MAX];
bool visited[MAX][MAX];
vector<int> ret;

int dfs(int y, int x) {
    int ret = 1;
    visited[y][x] = true;

    for (int i=0; i<4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (ny < 0 || nx < 0 || ny >= M || nx >= N || visited[ny][nx] == 1) continue;
        if (graph[ny][nx] == 1) continue;
        ret += dfs(ny, nx);
    }
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> M >> N >> K;
    for (int i=0; i<K; i++) {
        cin >> x1 >> y1 >> x2 >> y2;
        for (int x=x1; x<x2; x++) {
            for (int y=y1; y<y2; y++) {
                graph[y][x] = 1;
            }
        }
    }

    for (int i=0; i<M; i++) {
        for (int j=0; j<N; j++) {
            if (graph[i][j] != 1 && !visited[i][j]) {
                ret.push_back(dfs(i, j));
            }
        }
    }
    sort(ret.begin(), ret.end());
    cout << ret.size() << '\n';
    for (int r:ret) cout << r << ' ';

    return 0;
}