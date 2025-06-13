#include <bits/stdc++.h>
using namespace std;

const int MAX = 27;
const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {1, 0, -1, 0};
int R, C, y, x, ret;
bool visited[MAX];
char graph[MAX][MAX];
vector<int> v;

void dfs(int y, int x, int cnt) {
    ret = max(ret, cnt);
    for (int i=0; i<4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];
        if (ny < 0 || nx < 0 || ny >= R || nx >= C) continue;
        int next = (int)graph[ny][nx] - 'A';
        if (visited[next] == 0) {
            visited[next] = 1;
            dfs(ny, nx, cnt+1);
            visited[next] = 0;
        }
    }
    return;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> R >> C;
    for (int i=0; i<R; i++) {
        for (int j=0; j<C; j++) {
            cin >> graph[i][j];
        }
    }

    visited[(int)graph[0][0] - 'A'] = 1;
    dfs(0, 0, 1);
    
    cout << ret << '\n';
    return 0;
}