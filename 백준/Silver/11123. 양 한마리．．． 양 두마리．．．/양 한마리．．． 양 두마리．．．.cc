#include <bits/stdc++.h>
using namespace std;

const int MAX = 104;
const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {1, 0, -1, 0};
int T, H, W, y, x, ret;
char graph[MAX][MAX];
bool visited[MAX][MAX];

void bfs(int y, int x) {
    visited[y][x] = 1;
    queue<pair<int, int>> q;
    q.push({y, x});

    while(q.size()) {
        tie(y, x) = q.front();
        q.pop();
        for (int i=0; i<4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (ny < 0 || nx < 0 || ny >= H || nx >= W) continue;
            if (graph[ny][nx] == '.' || visited[ny][nx]) continue;
            visited[ny][nx] = 1;
            q.push({ny, nx});
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> T;
    while (T--) {
        ret = 0;
        memset(visited, 0, sizeof(visited));

        cin >> H >> W;
        for (int i=0; i<H; i++) {
            for (int j=0; j<W; j++) {
                cin >> graph[i][j];
            }
        }

        for (int i=0; i<H; i++) {
            for (int j=0; j<W; j++) {
                if (visited[i][j]) continue;
                if (graph[i][j] == '#') {
                    bfs(i, j);
                    ret++;
                }
            }
        }
        cout << ret << '\n';
    }
    return 0;
}