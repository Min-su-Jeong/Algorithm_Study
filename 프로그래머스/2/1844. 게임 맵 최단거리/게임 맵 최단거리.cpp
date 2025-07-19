#include<bits/stdc++.h>
using namespace std;

const int MAX = 101;
const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {-1, 0, 1, 0};
int n, m, visited[MAX][MAX], a[MAX][MAX];

int bfs(int y, int x, vector<vector<int>> &maps) {
    visited[y][x] = 1;
    queue<pair<int, int>> q;
    q.push({y, x});
    
    while (q.size()) {
        tie(y, x) = q.front();
        q.pop();
        for (int i=0; i<4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
            if (visited[ny][nx] || maps[ny][nx] == 0) continue;
            visited[ny][nx] = visited[y][x] + 1;
            q.push({ny, nx});
        }
    }
    return visited[n-1][m-1];
}

int solution(vector<vector<int>> maps)
{
    n = maps.size();
    m = maps[0].size();
    
    int ret = bfs(0, 0, maps);
    
    return ret != 0 ? ret : -1;
}