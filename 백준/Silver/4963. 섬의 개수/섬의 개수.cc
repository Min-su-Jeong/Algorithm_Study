#include <bits/stdc++.h>
using namespace std;

const int MAX = 54;
const int dx[8] = {1, 1, 0, -1, -1, -1, 0, 1};
const int dy[8] = {0, 1, 1, 1, 0, -1, -1, -1};
int w, h, y, x, ret, graph[MAX][MAX], visited[MAX][MAX];

void bfs(int y, int x) {
    visited[y][x] = 1;
    queue<pair<int, int>> q;
    q.push({y, x});

    while(q.size()) {
        tie(y, x) = q.front();
        q.pop();
        for (int i=0; i<8; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (ny < 0 || nx < 0 || ny >= h || nx >= w) continue;
            if (graph[ny][nx] == 0 || visited[ny][nx]) continue;
            visited[ny][nx] = 1;
            q.push({ny, nx});
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    while (true) {
        cin >> w >> h;
        if (w == 0 && h == 0) break;

        ret = 0;
        fill(&visited[0][0], &visited[0][0] + MAX * MAX, 0);
        for (int i=0; i<h; i++) {
            for (int j=0; j<w; j++) {
                cin >> graph[i][j];
            }
        }

        for (int i=0; i<h; i++) {
            for (int j=0; j<w; j++) {
                if (!graph[i][j] || visited[i][j]) continue;
                bfs(i, j);
                ret++;
            }
        }
        cout << ret << '\n';
    }
    return 0;
}