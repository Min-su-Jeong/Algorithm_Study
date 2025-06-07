#include <bits/stdc++.h>
using namespace std;

const int INIT = 987654321;
const int MAX = 1004;
const int dx[] = {0, -1, 0, 1};
const int dy[] = {1, 0, -1, 0};
int R, C, ret, sy, sx, x, y;
int fire[MAX][MAX], person[MAX][MAX];
char graph[MAX][MAX];

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL); cout.tie(NULL);

    queue<pair<int, int>> q;
    fill(&fire[0][0], &fire[0][0] + MAX * MAX, INIT);

    cin >> R >> C;
    for (int i=0; i<R; i++) {
        for (int j=0; j<C; j++) {
            cin >> graph[i][j];
            if (graph[i][j] == 'F') {
                fire[i][j] = 1;
                q.push({i, j});
            }
            else if (graph[i][j] == 'J') {
                sy = i;
                sx = j;
            }
        }
    }

    while (q.size()) {
        tie(y, x) = q.front(); q.pop();
        for (int i=0; i<4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (ny < 0 || nx < 0 || ny >= R || nx >= C) continue;
            if (fire[ny][nx] != INIT || graph[ny][nx] == '#') continue;
            fire[ny][nx] = fire[y][x] + 1;
            q.push({ny, nx});
        }
    }

    person[sy][sx] = 1;
    q.push({sy, sx});
    while (q.size()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        if (y == 0 || y == R-1 || x == 0 || x == C-1) {
            ret = person[y][x];
            break;
        }

        for (int i=0; i<4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (ny < 0 || nx < 0 || ny >= R || nx >= C) continue;
            if (person[ny][nx] || graph[ny][nx] == '#') continue;
            if (fire[ny][nx] <= person[y][x] + 1) continue;
            person[ny][nx] = person[y][x] + 1;
            q.push({ny, nx});
        }
    }
    if (ret == 0) cout << "IMPOSSIBLE\n";
    else cout << ret << '\n';

    return 0;
}