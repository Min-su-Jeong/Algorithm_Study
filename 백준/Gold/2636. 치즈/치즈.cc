#include <bits/stdc++.h>
using namespace std;

const int MAX = 104;
const int dx[4] = {1, -1, 0, 0};
const int dy[4] = {0, 0, 1, -1};
int r, c, ret1, ret2, graph[MAX][MAX];
bool visited[MAX][MAX];
vector<pair<int, int>> v;

void dfs(int y, int x) {
    visited[y][x] = 1;
    if (graph[y][x] == 1) {
        v.push_back({y, x});
        return;
    } 

    for (int i=0; i<4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];
        if (ny < 0 || nx < 0 || ny >= r || nx >= c || visited[ny][nx]) continue;
        dfs(ny, nx);
    }
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> r >> c;
    for (int i=0; i<r; i++) {
        for (int j=0; j<c; j++) {
            cin >> graph[i][j];
        }
    }

    while (true) {
        fill(&visited[0][0], &visited[0][0] + MAX * MAX, 0);
        v.clear();

        dfs(0, 0);
        ret2 = v.size(); 
        for (auto it: v) {
            graph[it.first][it.second] = 0;
        }

        bool flag = 0;
        for (int i=0; i<r; i++) {
            for (int j=0; j<c; j++) {
                if (graph[i][j] != 0) flag = 1;
            }
        }
        
        ret1++;
        if (!flag) break;
    }
    cout << ret1 << '\n' << ret2 << '\n';

    return 0;
}