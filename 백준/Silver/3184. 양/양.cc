#include <bits/stdc++.h>
using namespace std;

const int MAX=254;
const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {1, 0, -1, 0};
int R, C, cntW, cntS;
bool visited[MAX][MAX];
char graph[MAX][MAX];

void bfs(int y, int x) {
    int wolf = 0, sheep = 0;
    visited[y][x] = 1;
    if (graph[y][x] == 'v') wolf++;
    if (graph[y][x] == 'o') sheep++;

    queue<pair<int, int>> q;
    q.push({y, x});
    while (q.size()) {
        tie(y, x) = q.front();
        q.pop();
        for (int i=0; i<4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (ny < 0 || nx < 0 || ny >= R || nx >= C) continue;
            if (graph[ny][nx] == '#' || visited[ny][nx]) continue;
            if (graph[ny][nx] == 'v') wolf++;
            if (graph[ny][nx] == 'o') sheep++;
            visited[ny][nx] = 1;
            q.push({ny, nx});
        }
    }
    if (wolf < sheep) cntS += sheep;
    else cntW += wolf;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> R >> C;
    for (int i=0; i<R; i++) {
        for (int j=0; j<C; j++) {
            cin >> graph[i][j];
        }
    }

    for (int i=0; i<R; i++) {
        for (int j=0; j<C; j++) {
            if (visited[i][j] || graph[i][j] == '#') continue;
            bfs(i, j);
        }
    }

    cout << cntS << ' ' << cntW << '\n';
    
    return 0;
}