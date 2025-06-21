#include <bits/stdc++.h>
using namespace std;

const int MAX = 1504;
const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {1, 0, -1, 0};
int R, C, y, x, sy, sx, ret;
char graph[MAX][MAX];
bool swan[MAX][MAX], water[MAX][MAX];
queue<pair<int, int>> waterQ, waterTmpQ, swanQ, swanTmpQ;
string s;

void meltWater() {
    while (waterQ.size()) {
        tie(y, x) = waterQ.front();
        waterQ.pop();
        for (int i=0; i<4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (ny < 0 || nx < 0 || ny >= R || nx >= C || water[ny][nx]) continue;
            if (graph[ny][nx] == 'X') {
                water[ny][nx] = 1;
                graph[ny][nx] = '.';
                waterTmpQ.push({ny, nx});
            }
        }
    }
}

bool moveSwan() {
    while (swanQ.size()) {
        tie(y, x) = swanQ.front();
        swanQ.pop();
        for (int i=0; i<4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (ny < 0 || nx < 0 || ny >= R || nx >= C || swan[ny][nx]) continue;
            swan[ny][nx] = 1;
            if (graph[ny][nx] == 'L') return true;
            if (graph[ny][nx] == '.') swanQ.push({ny, nx});
            if (graph[ny][nx] == 'X') swanTmpQ.push({ny, nx});
        }
    }
    return false;
}

void clearQ(queue<pair<int, int>> &q) {
    queue<pair<int, int>> empty;
    swap(q, empty);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin>> R >> C;
    for (int i=0; i<R; i++) {
        cin >> s;
        for (int j=0; j<C; j++) {
            graph[i][j] = s[j];
            if (graph[i][j] == 'L') { sy = i, sx = j; }
            if (graph[i][j] == '.' || graph[i][j] == 'L') {
                waterQ.push({i, j});
                water[i][j] = 1;
            }
        }
    }

    swanQ.push({sy, sx});
    swan[sy][sx] = 1;
    while (true) {
        if (moveSwan()) break;
        meltWater();
        waterQ = waterTmpQ;
        swanQ = swanTmpQ;
        clearQ(waterTmpQ);
        clearQ(swanTmpQ);
        ret++;
    }

    cout << ret << '\n';
    return 0;
}