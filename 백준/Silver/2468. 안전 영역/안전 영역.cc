#include <bits/stdc++.h>
using namespace std;

const int MAX = 104;
const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {-1, 0, 1, 0};
int N, a[MAX][MAX], ret=1;
bool visited[MAX][MAX];

void bfs(int y, int x, int h) {
    queue<pair<int, int>> q;
    q.push({y, x});

    while (q.size()) {
        tie(y, x) = q.front();
        q.pop();
        for (int i=0; i<4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (ny < 0 || ny >= N || nx < 0 || nx >= N) continue;
            if (visited[ny][nx] || a[ny][nx] <= h) continue;
            visited[ny][nx] = 1;
            q.push({ny, nx});
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> a[i][j];
        }
    }

    for (int h=1; h<=100; h++) {
        int cnt = 0;
        memset(visited, 0, sizeof(visited));
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                if (a[i][j] > h) {
                    if (visited[i][j]) continue;
                    visited[i][j] = 1;
                    bfs(i, j, h);
                    cnt++;
                }
            }
        }
        ret = max(ret, cnt);
    }
    cout << ret << '\n';
    
    return 0;
}