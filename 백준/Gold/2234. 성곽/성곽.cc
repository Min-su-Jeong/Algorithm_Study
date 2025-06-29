#include <bits/stdc++.h>
using namespace std;

const int MAX = 51;
const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {-1, 0, 1, 0}; 
int N, M, cnt, mx, biggest, roomSize[MAX*MAX], a[MAX][MAX], visited[MAX][MAX];

int dfs(int x, int y, int roomNum) {
    if (visited[x][y]) return 0;
    visited[x][y] = roomNum;
    int ret = 1;
    
    for (int i = 0; i < 4; i++) {
        if (!(a[x][y] & (1 << i))) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && nx < M && ny >= 0 && ny < N) {
                ret += dfs(nx, ny, roomNum);
            }
        }
    }
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M;
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            cin >> a[i][j];
        }
    }

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            if (!visited[i][j]) {
                cnt++;
                roomSize[cnt] = dfs(i, j, cnt);
                mx = max(mx, roomSize[cnt]);
            }
        }
    }

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            if (i + 1 < M) {
                int room1 = visited[i][j];
                int room2 = visited[i+1][j];
                if (room1 != room2) {
                    biggest = max(biggest, roomSize[room1] + roomSize[room2]);
                }
            }
            if (j + 1 < N) {
                int room1 = visited[i][j];
                int room2 = visited[i][j+1];
                if (room1 != room2) {
                    biggest = max(biggest, roomSize[room1] + roomSize[room2]);
                }
            }
        }
    }
    
    cout << cnt << '\n' << mx << '\n' << biggest << '\n';
    return 0;
}