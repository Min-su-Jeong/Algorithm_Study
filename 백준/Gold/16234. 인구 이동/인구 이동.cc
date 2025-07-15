#include <bits/stdc++.h>
using namespace std;

const int MAX = 54;
const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {1, 0, -1, 0};
int N, L, R, sum, ret, a[MAX][MAX];
bool visited[MAX][MAX];
vector<pair<int, int>> v;

void dfs(int y, int x) {
    for (int i=0; i<4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];
        if (ny < 0 || ny >= N || nx < 0 || nx >= N || visited[ny][nx]) continue;
        int gap = abs(a[ny][nx] - a[y][x]);
        if (L <= gap && gap <= R) {
            visited[ny][nx] = 1;
            sum += a[ny][nx];
            v.push_back({ny, nx});
            dfs(ny, nx);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> L >> R;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> a[i][j];
        }
    }

    while (true) {
        bool flag = 0;
        memset(visited, 0, sizeof(visited));

        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                if (visited[i][j]) continue;
                v.clear();
                v.push_back({i, j});
                visited[i][j] = 1;
                sum = a[i][j];
                dfs(i, j);

                if (v.size() == 1) continue;
                
                int area = sum / v.size();
                for (auto it: v) a[it.first][it.second] = area;
                flag = 1;
            }
        }
        if (!flag) break;
        ret++;
    }
    cout << ret << '\n';

    return 0;
}